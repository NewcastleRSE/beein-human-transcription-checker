function highlightErrorToggle(errorId) {
    const errorItem = document.getElementById(errorId.toString());
    const errorIdCorrected = errorId.toString().replace(/\D/g,'');
    const searchString = '[id*="' + errorIdCorrected + '"]'
    const error = document.getElementById(document.querySelector(searchString).id)
    if (error.classList.contains('active')) {
        error.classList.remove('active');
        errorItem.classList.remove('selected')
    } else {
        error.classList.add("active");
        errorItem.classList.add('selected')
        error.scrollIntoView();
    }
}

function transferEditedText() {
    const text = document.getElementById('text').textContent
    document.getElementById('text-form').textContent = text
}