
function createSnowflake() {
            const snowflake = document.createElement("div");
            snowflake.classList.add("snowflake");
            snowflake.innerHTML = "🌸";
            document.body.appendChild(snowflake);

            const startLeft = Math.random() * window.innerWidth;
            const endLeft = Math.random() * window.innerWidth;
            const duration = Math.random() * 3 + 2;
            const size = Math.random() * 20 + 10;

            snowflake.style.left = `${startLeft}px`;
            snowflake.style.fontSize = `${size}px`;
            snowflake.style.opacity = Math.random();
            snowflake.style.position = "fixed";

            const keyframes = [
                { transform: `translateY(0px)`, left: `${startLeft}px` },
                { transform: `translateY(${window.innerHeight}px)`, left: `${endLeft}px` }
            ];

            snowflake.animate(keyframes, {
                duration: duration * 1000,
                easing: "linear",
                iterations: 1
            });

            setTimeout(() => {
                snowflake.remove();
            }, duration * 1000);
}
setInterval(createSnowflake, 200);
