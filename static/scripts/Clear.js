document.getElementById('clearBoardButton').addEventListener('click', async () => {
    startCell = { row: 6, col: 8 };
    endCell = { row: 6, col: 30 };
    const infoPanel = document.querySelector('.info-panel');
    
    // Remove all child elements except the first (the welcome message)
    while (infoPanel.children.length > 1) {
        infoPanel.removeChild(infoPanel.lastChild);
    }
    createGrid();

});

document.getElementById('clearPathButton').addEventListener('click', () => {
    document.querySelectorAll('.path').forEach(cell => {
        cell.classList.remove('path');
    })
})