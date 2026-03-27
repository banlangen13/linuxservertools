// 菜单点击切换页面
document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', function() {
        // 去掉所有菜单高亮
        document.querySelectorAll('.menu-item').forEach(i => i.classList.remove('active'));
        // 当前菜单高亮
        this.classList.add('active');

        // 获取对应页面ID
        const pageId = this.getAttribute('data-page');
        // 隐藏所有页面
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        // 显示目标页面
        document.getElementById(pageId).classList.add('active');
    });
});