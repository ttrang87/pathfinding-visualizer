export function statusCell() {
    const rows = defaultrows
    const cols = defaultcols
    const maze_status = [];

    for (let r = 0; r < rows; r++) {
        maze_status[r] = []
        for (let c = 0; c < cols; c++) {
            const cell = document.querySelector(`[data-row='${r}'][data-col='${c}']`);
            maze_status[r][c] = cell.classList.contains("maze-cell") ? 1 : 0;
        }
    }

    return maze_status;
}