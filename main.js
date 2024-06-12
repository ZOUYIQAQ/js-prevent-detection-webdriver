// 使用代理来拦截对 navigator 对象的访问
(function() {
    // 通过代理对象来拦截并隐藏 webdriver 属性
    const newNavigator = new Proxy(navigator, {
        has: (target, key) => (key === 'webdriver' ? false : key in target),
        get: (target, key) => (key === 'webdriver' ? undefined : target[key])
    });
    Object.defineProperty(window, 'navigator', {
        value: newNavigator,
        configurable: false,
        enumerable: true,
        writable: false
    });
})();
