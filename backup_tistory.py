import feedparser
import os
import json
import re
from datetime import datetime
from pathlib import Path
from collections import defaultdict

def sanitize_filename(title):
    """파일명으로 사용할 수 있도록 제목 정리"""
    # 특수문자 제거 및 공백을 하이픈으로 변경
    title = re.sub(r'[<>:"/\\|?*]', '', title)
    title = re.sub(r'\s+', '-', title)
    return title[:100]  # 파일명 길이 제한

def sanitize_category(category):
    """카테고리명을 폴더명으로 사용할 수 있도록 정리"""
    if not category:
        return "uncategorized"
    # 특수문자 제거 및 공백을 하이픈으로 변경
    category = re.sub(r'[<>:"/\\|?*]', '', category)
    category = re.sub(r'\s+', '-', category)
    return category[:50]  # 폴더명 길이 제한

def download_tistory_posts():
    """Tistory RSS에서 포스트 다운로드"""
    blog_url = os.environ.get('TISTORY_BLOG_URL', '')
    
    if not blog_url:
        print("❌ TISTORY_BLOG_URL 환경변수가 설정되지 않았습니다.")
        return
    
    # RSS 피드 URL (끝에 슬래시 제거)
    blog_url = blog_url.rstrip('/')
    rss_url = f"{blog_url}/rss"
    
    print(f"✅ 블로그 URL: {blog_url}")
    print(f"✅ RSS 피드 확인: {rss_url}")
    
    feed = feedparser.parse(rss_url)
    
    # RSS 피드 상태 확인
    print(f"✅ RSS 피드 상태: {feed.get('status', 'unknown')}")
    print(f"✅ 피드 버전: {feed.get('version', 'unknown')}")
    print(f"✅ 총 엔트리 수: {len(feed.entries)}")
    
    if not feed.entries:
        print("❌ RSS 피드에서 포스트를 찾을 수 없습니다.")
        print(f"   피드 제목: {feed.feed.get('title', 'N/A')}")
        print(f"   에러 여부: {feed.get('bozo', False)}")
        if feed.get('bozo'):
            print(f"   에러 내용: {feed.get('bozo_exception', 'N/A')}")
        return
    
    # 백업 디렉토리 생성
    backup_dir = Path('posts')
    backup_dir.mkdir(exist_ok=True)
    
    # 메타데이터 파일
    metadata_file = backup_dir / 'metadata.json'
    
    # 기존 메타데이터 로드
    if metadata_file.exists():
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
    else:
        metadata = {}
    
    new_posts = 0
    
    for entry in feed.entries:
        post_id = entry.get('id', entry.link)
        
        # 이미 백업된 포스트는 건너뛰기
        if post_id in metadata:
            continue
        
        # 포스트 정보 추출
        title = entry.get('title', 'Untitled')
        published = entry.get('published', '')
        content = entry.get('description', '')
        link = entry.get('link', '')
        
        # 티스토리 카테고리 추출
        # feedparser에서는 entry.tags 리스트로 카테고리를 제공
        category = 'uncategorized'
        
        if hasattr(entry, 'tags') and entry.tags:
            # 첫 번째 태그를 카테고리로 사용
            category = entry.tags[0].get('term', 'uncategorized')
            print(f"  카테고리 발견: {category}")
        
        # 디버그: 사용 가능한 모든 속성 출력 (처음 한 번만)
        if new_posts == 0:
            print(f"\n[디버그] 엔트리 속성: {dir(entry)}")
            if hasattr(entry, 'tags'):
                print(f"[디버그] 태그 정보: {entry.tags}")
        
        # 카테고리 폴더 생성
        safe_category = sanitize_category(category)
        category_dir = backup_dir / safe_category
        category_dir.mkdir(exist_ok=True)
        
        # 파일명 생성
        safe_title = sanitize_filename(title)
        
        # 날짜 파싱
        try:
            pub_date = datetime.strptime(published, '%a, %d %b %Y %H:%M:%S %z')
            date_str = pub_date.strftime('%Y-%m-%d')
            timestamp = pub_date.timestamp()
        except:
            date_str = datetime.now().strftime('%Y-%m-%d')
            timestamp = datetime.now().timestamp()
        
        filename = f"{date_str}_{safe_title}.md"
        filepath = category_dir / filename
        
        # 마크다운 형식으로 저장
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**카테고리**: {category}\n\n")
            f.write(f"**작성일**: {published}\n\n")
            f.write(f"**원문 링크**: {link}\n\n")
            f.write("---\n\n")
            f.write(content)
        
        # 메타데이터 업데이트
        metadata[post_id] = {
            'title': title,
            'category': category,
            'published': published,
            'timestamp': timestamp,
            'link': link,
            'filename': filename,
            'folder': safe_category,
            'backed_up_at': datetime.now().isoformat()
        }
        
        new_posts += 1
        print(f"새 포스트 백업: [{category}] {title}")
    
    # 메타데이터 저장
    with open(metadata_file, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, ensure_ascii=False, indent=2)
    
    print(f"\n총 {new_posts}개의 새 포스트를 백업했습니다.")
    
    # README 업데이트
    update_readme(metadata)

def update_readme(metadata):
    """README 파일 생성/업데이트 - 최신순, 카테고리별 정렬"""
    readme_path = Path('README.md')
    
    # 카테고리별로 포스트 그룹화
    posts_by_category = defaultdict(list)
    
    for post in metadata.values():
        category = post.get('category', 'uncategorized')
        posts_by_category[category].append(post)
    
    # 각 카테고리 내에서 최신순 정렬
    for category in posts_by_category:
        posts_by_category[category].sort(
            key=lambda x: x.get('timestamp', 0),
            reverse=True  # 최신순
        )
    
    # 전체 포스트를 최신순으로 정렬
    all_posts_sorted = sorted(
        metadata.values(),
        key=lambda x: x.get('timestamp', 0),
        reverse=True  # 최신순
    )
    
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# Tistory 블로그 백업\n\n")
        f.write(f"총 {len(metadata)}개의 포스트가 백업되었습니다.\n\n")
        f.write(f"마지막 업데이트: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # 전체 포스트 목록 (최신순)
        f.write("## 📝 최근 포스트 (최신순)\n\n")
        for post in all_posts_sorted[:10]:  # 최근 10개만 표시
            title = post.get('title', 'Untitled')
            link = post.get('link', '')
            published = post.get('published', '')
            category = post.get('category', 'uncategorized')
            folder = post.get('folder', 'uncategorized')
            filename = post.get('filename', '')
            
            f.write(f"- **[{category}]** [{title}]({link})\n")
            f.write(f"  - 📅 {published}\n")
            f.write(f"  - 📁 `posts/{folder}/{filename}`\n\n")
        
        # 카테고리별 포스트 목록
        f.write("\n## 📂 카테고리별 포스트\n\n")
        
        # 카테고리를 포스트 개수로 정렬
        sorted_categories = sorted(
            posts_by_category.items(),
            key=lambda x: len(x[1]),
            reverse=True
        )
        
        for category, posts in sorted_categories:
            f.write(f"### {category} ({len(posts)}개)\n\n")
            
            for post in posts:
                title = post.get('title', 'Untitled')
                link = post.get('link', '')
                published = post.get('published', '')
                folder = post.get('folder', 'uncategorized')
                filename = post.get('filename', '')
                
                f.write(f"- [{title}]({link})\n")
                f.write(f"  - 📅 {published}\n")
                f.write(f"  - 📁 `posts/{folder}/{filename}`\n\n")
        
        # 통계
        f.write("\n## 통계\n\n")
        f.write(f"- 총 포스트: {len(metadata)}개\n")
        f.write(f"- 카테고리: {len(posts_by_category)}개\n\n")
        
        f.write("### 카테고리별 포스트 수\n\n")
        for category, posts in sorted_categories:
            f.write(f"- {category}: {len(posts)}개\n")

if __name__ == '__main__':
    download_tistory_posts()