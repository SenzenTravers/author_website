/////////// INITIALIZE CUSTOM MODULES
class Counter {
    constructor(quill, options) {
        this.quill = quill;
        this.options = options;
        this.container = document.querySelector(options.container);
        quill.on(Quill.events.TEXT_CHANGE, this.update.bind(this));
    }

    calculate() {
        const text = this.quill.getText();

        if (this.options.unit === 'word') {
        const trimmed = text.trim();
        // Splitting empty text returns a non-empty array
        return trimmed.length > 0 ? trimmed.split(/\s+/).length : 0;
        } else {
        return text.length - 1;
        }
    }

    update() {
        const length = this.calculate();
        let label = this.options.unit;
        if (length !== 1) {
        label += 's';
        }
        this.container.innerText = `${length} ${label}`;
        if (length >= this.options.charLimit) {
            this.container.classList.add("limit-reached")
            this.container.innerText += ` : attention ! La limite acceptée est de ${this.options.charLimit} caractères.`
        } else {
            this.container.classList.remove("limit-reached")
        }
    }
    }

Quill.register('modules/counter', Counter);

//////////////////////// EDITORS
let quillSummary = new Quill('#quill-summary', {
    modules: {
        toolbar: [
            [
                'bold', 'italic', 'underline','strike',
                { 'align': [] },
                { 'list': 'ordered'}, { 'list': 'bullet' },
                'link'
            ],
        ],
        history: {
            delay: 1000,
            maxStack: 200,
            userOnly: false
        },
        counter: {
            container: '#char-counter-summary',
            unit: 'caractère',
            charLimit: 600,
        }
    },
    placeholder: '',
    theme: 'snow'
});

let quillFicAuthorNote = new Quill('#quill-fic-author-note', {
    modules: {
        toolbar: [
            'bold', 'italic', 'underline','strike',
            { 'align': [] },
            { 'list': 'ordered'}, { 'list': 'bullet' },
            'link'
        ],
        history: {
            delay: 1000,
            maxStack: 200,
            userOnly: false
        },
        counter: {
            container: '#char-counter-fic-author-note',
            unit: 'caractère',
            charLimit: 2000
        }
    },
    placeholder: '',
    theme: 'snow'
});
let quillChapterAuthorNote = new Quill('#quill-chapter-author-note', {
    modules: {
        toolbar: [
            'bold', 'italic', 'underline','strike',
            { 'align': [] },
            { 'list': 'ordered'}, { 'list': 'bullet' },
            'link'
        ],
        history: {
            delay: 1000,
            maxStack: 200,
            userOnly: false
        },
        counter: {
            container: '#char-counter-chapter-author-note',
            unit: 'caractère',
            charLimit: 1500
        }
    },
    placeholder: '',
    theme: 'snow'
});
let quillContent = new Quill('#quill-content', {
    modules: {
        toolbar: [
            'bold', 'italic', 'underline','strike',
            { 'align': [] },
            { 'list': 'ordered'}, { 'list': 'bullet' },
            'link'
        ],
        history: {
            delay: 1000,
            maxStack: 200,
            userOnly: false
        },
        counter: {
            container: '#char-counter-content',
            unit: 'caractère',
            charLimit: 1000000
        }
    },
    placeholder: '',
    theme: 'snow'
});
/////////// FUELLING THE QUILL DATA TO THE FORM
quillSummary.on('text-change', function(delta, source) {
    onQuillEditorChange("summary", 600)
})
quillFicAuthorNote.on('text-change', function(delta, source) {
    onQuillEditorChange("fic-author-note", 2000)
})
quillChapterAuthorNote.on('text-change', function(delta, source) {
    onQuillEditorChange("author-note", 1500)
})
quillContent.on('text-change', function(delta, source) {
    onQuillEditorChange("content", 1000000)
})


function onQuillEditorChange(editorName) {
    handleCharacterLimit(editorName, 1000000)
    updateHtmlOutput(editorName)
} 

function updateHtmlOutput(editorName) {
    let html = getQuillHtml(editorName);
    editorName = editorName.replace('-', '_')
    editorName = editorName.replace('-', '_')
    document.getElementById('id_'+editorName).innerText = html;
}

function getQuillHtml(editorName) {
    let editor = ""
    if (editorName == "summary") {
        editor = quillSummary
    } else if (editorName == "fic-author-note") {
        editor = quillFicAuthorNote
    } else if (editorName == "author-note") {
        editor = quillChapterAuthorNote
    } else if (editorName == "content") {
        editor = quillContent
    } else {
        return;
    }
    return editor.root.innerHTML;
}

quillSummary.clipboard.dangerouslyPasteHTML(ficAuthorNoteValue);
quillFicAuthorNote.clipboard.dangerouslyPasteHTML(ficSummaryValue);
quillChapterAuthorNote.clipboard.dangerouslyPasteHTML(chapterAuthorNoteValue);
quillContent.clipboard.dangerouslyPasteHTML(chapterContentValue);


////// GENERAL EDITOR FUNCTIONS
function handleCharacterLimit(editorName, limit) {
    let editor = ""
    if (editorName == "summary") {
        editor = quillSummary
    } else if (editorName == "fic-author-note") {
        editor = quillFicAuthorNote
    } else if (editorName == "author-note") {
        editor = quillChapterAuthorNote
    } else if (editorName == "content") {
        editor = quillContent
    }
    if (editor.getLength() > limit) {
        editor.history.undo();
    }
}
