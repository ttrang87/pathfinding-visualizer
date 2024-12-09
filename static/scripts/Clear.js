document.getElementById('clearBoardButton').addEventListener('click', async () => {
    startCell = { row: 3, col: 4 };
    endCell = { row: 10, col: 27 };
    createGrid();

});

document.getElementById('clearPathButton').addEventListener('click', () => {
    document.querySelectorAll('.path').forEach(cell => {
        cell.classList.remove('path');
    })
})