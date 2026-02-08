// 마크다운 콘텐츠의 계층적 들여쓰기
document.addEventListener('DOMContentLoaded', function() {
  const prose = document.querySelector('.prose');
  if (!prose) return;

  let currentLevel = 0;
  const elements = prose.querySelectorAll('h2, h3, h4, p, ul, ol, pre, blockquote, table');
  
  elements.forEach(el => {
    const tagName = el.tagName.toLowerCase();
    
    if (tagName === 'h2') {
      currentLevel = 2;
      el.style.marginLeft = '1rem';
    } else if (tagName === 'h3') {
      currentLevel = 3;
      el.style.marginLeft = '2rem';
    } else if (tagName === 'h4') {
      currentLevel = 4;
      el.style.marginLeft = '3rem';
    } else {
      // 본문 요소
      if (currentLevel === 2) {
        el.style.marginLeft = '2rem';
      } else if (currentLevel === 3) {
        el.style.marginLeft = '3rem';
      } else if (currentLevel === 4) {
        el.style.marginLeft = '4rem';
      }
    }
  });
});
