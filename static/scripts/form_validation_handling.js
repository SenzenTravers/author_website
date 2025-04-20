document.addEventListener('click', function() {
    checkRequiredFields(
        ["id_pairing_type", "id_rating", "id_complete", "id_fic_title", "id_summary", "id_content"]
    )
});

function checkRequiredFields(requiredFields) {
    const allRequired = []
    let missing = []

    requiredFields.forEach(function (fieldId) {
        let element = document.getElementById(fieldId)
        allRequired.push(element);
      }
    );
    allRequired.forEach(function (element) {
        if (('', null, "undefined").includes(element.value) && element.id !== "id_pairing_type") {
            missing.push(element)
        }
      }
    );

    pairingTypeChecked = handleMultiChoices("id_pairing_type", 5)
    if (missing.length === 0 && pairingTypeChecked) {
        ficSubmitBtn.disabled = false 
    } else {
        ficSubmitBtn.disabled = true
    }
}

function handleMultiChoices(mainId, elementLength) {
    let choicesRange = Array(elementLength).fill(0).map((_, i) => i++);
    let checked = []
    choicesRange.forEach(function (i) {
        let inputItem = document.getElementById(mainId + "_" + i)
        if (inputItem.checked) {
            checked.push(inputItem)
        }
    })

    if (checked.length > 0) {
        return true;
    } else {
        return false;
    } 
    
}