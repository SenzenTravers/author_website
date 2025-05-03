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
        // SEN : tu as aussi changé ceci. Teste et implante si ça fonctionne bien
        this.container.innerText = `${length} ${label}/${this.options.charLimit}`;
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
let quillSummary;
let quillFicAuthorNote;
let quillChapterAuthorNote;
let quillContent;

try {
    quillSummary = new Quill('#quill-summary', {
        modules: {
            toolbar: [
                [
                    'bold', 'italic', 'underline','strike',
                    { align: 'center' }, { align: 'right' }, { align: 'justify' },
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
        formats: [
            'bold', 'italic', 'underline','strike', 'link',
            'list', 'align'
        ],
        theme: 'snow'
    });    
} catch {
    console.log("Summary quill not initialized.")
}

try {
    quillFicAuthorNote = new Quill('#quill-fic-author-note', {
        modules: {
            toolbar: [
                'bold', 'italic', 'underline','strike',
                { align: 'center' }, { align: 'right' }, { align: 'justify' },
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
        formats: [
            'bold', 'italic', 'underline','strike', 'link',
            'list', 'align'
        ],
        theme: 'snow'
    });
} catch {
    console.log("Author quill not initialized.")
}

try {
    quillChapterAuthorNote = new Quill('#quill-chapter-author-note', {
        modules: {
            toolbar: [
                'bold', 'italic', 'underline','strike',
                { align: 'center' }, { align: 'right' }, { align: 'justify' },
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
        formats: [
            'bold', 'italic', 'underline','strike', 'link',
            'list', 'align'
        ],
        theme: 'snow'
    });
} catch {
    console.log("Chapter note quill not initialized.")
}
try {quillContent = new Quill('#quill-content', {
    modules: {
        toolbar: [
            'bold', 'italic', 'underline','strike',
            { align: 'center' }, { align: 'right' }, { align: 'justify' },
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
        formats: [
            'bold', 'italic', 'underline','strike', 'link',
            'list', 'align'
        ],
        theme: 'snow'
});
} catch {
    console.log("Content quill not initialized.")
}

/////////// FUELLING THE QUILL DATA TO THE FORM
if (quillSummary) {
    quillSummary.on('text-change', function(delta, source) {
        onQuillEditorChange("summary", 600)
    })
    quillSummary.clipboard.dangerouslyPasteHTML(ficSummaryValue);
}

if (quillFicAuthorNote) {
    quillFicAuthorNote.on('text-change', function(delta, source) {
        onQuillEditorChange("fic-author-note", 2000)
    })
    quillFicAuthorNote.clipboard.dangerouslyPasteHTML(ficAuthorNoteValue);
}

if (quillChapterAuthorNote) {
    quillChapterAuthorNote.on('text-change', function(delta, source) {
        onQuillEditorChange("author-note", 1500)
    })
    quillChapterAuthorNote.clipboard.dangerouslyPasteHTML(chapterAuthorNoteValue);
}

if (quillContent) {
    quillContent.on('text-change', function(delta, source) {
        onQuillEditorChange("content", 1000000)
    })
    quillContent.clipboard.dangerouslyPasteHTML(chapterContentValue);
}


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
