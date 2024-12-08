document.getElementById('RandomObstacleButton').addEventListener('click', () => {
    for (let r = 0; r < defaultrows; r++) {
        for (let c = 0; c < defaultcols; c++) {
            const cell = document.querySelector(`[data-row='${r}'][data-col='${c}']`);
            cell.addEventListener('click', () => { cell.classList.toggle('maze-cell')}); // Avoid duplicating listeners
        }
    }
});
