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

function hideTranscription() {
    const transcription = document.getElementById('text');
    const hideBtn = document.getElementById('hideTransc')

    if (transcription.style.display == 'none') {
        transcription.style.display = 'block';
        hideBtn.innerHTML  = 'Hide Transcription';
    } else {
        transcription.style.display = 'none';
        hideBtn.innerHTML = 'Show Transcription';
    };
}

function toggleHideTranscriptionButton() {
    const transcription = document.getElementById('converted-text');
    const hideBtn = document.getElementById('hideTransc')

    if (typeof(transcription) != 'undefined' && transcription != null) {
        hideBtn.style.display = 'block';
    }
}

window.onload = function() {
    toggleHideTranscriptionButton();
}