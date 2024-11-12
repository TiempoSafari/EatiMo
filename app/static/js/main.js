// 处理收藏功能
function toggleFavorite(recipeId) {
    fetch('/api/recipes/favorite', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            recipe_id: recipeId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            // 更新UI显示
            const btn = event.target.closest('.favorite-btn');
            btn.classList.toggle('text-yellow-500');
        }
    });
} 