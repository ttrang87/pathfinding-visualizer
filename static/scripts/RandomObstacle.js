document.getElementById('RandomObstacleButton').addEventListener('click', async () => {
    for (let r = 0; r < defaultrows; r++) {
        for (let c = 0; c < defaultcols; c++) {
            const cell = document.querySelector(`[data-row='${r}'][data-col='${c}']`);
            cell.addEventListener("click", () => {
                cell.classList.toggle('maze-cell'); //classList.toggle(): if this class exists, remove it. else, add it
            });
        }
    }
});
