export function updateInfor(algorithm, visited_cells, time, path) {
    const infoPanel = document.querySelector('.info-panel');
    const info = document.createElement('div'); 
    const roundedTime = time.toFixed(3);
    info.textContent = `${algorithm} visited ${visited_cells.length} cells in ${roundedTime} ms. Path length = ${path.length}`;
    infoPanel.appendChild(info);
}

export function scrollToBottom() {
    const infoPanel = document.querySelector('.info-panel');
    infoPanel.scrollTop = infoPanel.scrollHeight;
}

export function showToast(message) {
    const toast = document.createElement('div');
    toast.classList.add('toast');
    toast.textContent = message;

    const toastContainer = document.getElementById('toast-container');
    toastContainer.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 3500);
}

