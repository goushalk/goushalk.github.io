document.addEventListener('mousemove', function(e) {
    const char = String.fromCharCode(Math.floor(Math.random() * 94) + 33);
    const span = document.createElement('span');
    span.textContent = char;
    span.style.position = 'absolute';
    span.style.left = `${e.pageX}px`;
    span.style.top = `${e.pageY}px`;
    span.style.fontSize = '20px';
    span.style.color = `lime`;
    document.body.appendChild(span);

    setTimeout(() => {
        span.remove();
    }, 150);
});


