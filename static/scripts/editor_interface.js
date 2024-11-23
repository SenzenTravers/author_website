    // STARTING VARIABLES
    let currentLength = 0;
    let ongoingSprint = 0;
    let lastEditDate = ""
    let lastKnownValue = ""
    let timeSpentWriting = 0
    const modalDialog = document.querySelector("dialog");

    if (sessionStorage.getItem("textAutosave")) {
      document.getElementById("text-input").innerHTML = sessionStorage.getItem("textAutosave");
    }
      
    ///////////////// MAIN COUNTDOWN HANDLING FUNCTION
    function handleCountDown() {
      let minutes = returnDelayValue()
      document.getElementById("startCdBtn").disabled = true      
      document.getElementById("stopCdBtn").disabled = false

      if (minutes == 0) { // Then, do nothing
        return 0
      }

      ongoingSprint = 1
      let countDownDate = addSecondsToNow(minutes*60)

      // Update the count down every 1 second
      // TODO: for a "pause" button, just add one second to countDownDate every second
      let timerInterval = setInterval(function() {

        if (ongoingSprint == 0) {
          handleCdEnding(timerInterval)
          return
        }

        let now = new Date().getTime();
        // Find the distance between now and the count down date
        let distance = countDownDate - now;

        let visibleTimerContent = returnVisibleTimerContent(distance)

        watchAndHandleChanges()
        handleWorkingTime(now)

        document.getElementById("visible-timer").innerHTML = visibleTimerContent

        if (distance < 0) {
          playAudio("victoryAudio")
          handleCdEnding(timerInterval)
        }
      }, 1000);
    }


    // UTILS FUNCTIONS
    function addSecondsToNow(value) {
      let nowTimeObject = new Date();
      const milliseconds = value * 1000; // 10 seconds = 10000 milliseconds

      return new Date(nowTimeObject.getTime() + milliseconds);
    }

    function handleCdEnding(timerInterval) {
      clearInterval(timerInterval);

      document.getElementById("visible-timer").innerHTML = "Aucune session en cours pour l'instant."
      document.getElementById("startCdBtn").disabled = false
      document.getElementById("stopCdBtn").disabled = true

      if (timeSpentWriting > 0) {
        const minutes = Math.floor((timeSpentWriting/60))
        const seconds = Math.floor((timeSpentWriting % 60));
        const visibleMinutes = minutes? minutes + "mn et ": ""
        const visibleSeconds = seconds + "s"
        const msg = "Félicitations ! Vous avez écrit " + visibleMinutes + visibleSeconds + " au total."

        document.getElementById("timer-dialog-content").textContent = msg
        modalDialog.showModal();
      }

      lastEditDate = ""
      lastKnownValue = ""
      timeSpentWriting = 0
    }

    function handleTimerLengthChange() {
        let value = returnDelayValue()
        let btn = document.getElementById("startCdBtn")

        if (value != 0) {
          btn.disabled = false
        } else {
          btn.disabled = true
        }

    }

    function handleWorkingTime(currentTime) {
      if ((currentTime - lastEditDate) < 15000) {
        timeSpentWriting += 1
      }
    }

    function returnNumberOfWords(contentBlock){
        const regex = /[\p{L}\p{M}\d-]+/ugm;
        const found = contentBlock.textContent.match(regex);

        return found? found.length: 0

    }

    function returnVisibleTimerContent(distance) {
      let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      let seconds = Math.floor((distance % (1000 * 60)) / 1000);
      let visibleHours = hours? hours + "h": ""

      return visibleHours + minutes + "m" + seconds + "s";
    }

    function watchAndHandleChanges() {
      let newText = document.getElementById("text-input").textContent
      
      if (newText != lastKnownValue) {
        lastKnownValue = newText
        lastEditDate = new Date().getTime();
        sessionStorage.setItem("textAutosave", newText)
      }
    }

    function stopCountdown() {
      ongoingSprint = 0
    }

    function exportInputText() {
      let textToExport = document.getElementById('text-input').innerHTML
      textToExport = textToExport.replaceAll("<div>", "<p>")
      textToExport = textToExport.replaceAll("</div>", "</p>")
      textToExport = textToExport.replaceAll("<br>", "")
      textToExport = textToExport.replaceAll("line-height: 100%;", "")
      textToExport = textToExport.replaceAll("margin-bottom: 0cm;", "")
      textToExport = textToExport.replaceAll("line-height: 100%", "")
      textToExport = textToExport.replaceAll("margin-bottom: 0cm", "")
      textToExport = textToExport.replaceAll('style=" "', "")
      navigator.clipboard.writeText(textToExport)
      document.getElementById("timer-dialog-content").textContent = "Votre texte a bien été copié."
      modalDialog.showModal()
    }
    //////////////// UTILS DOM-RELATED FUNCTIONS
    function returnDelayValue() {
      let valueInput = document.getElementById("timer-length").value
      valueInput = Number(valueInput)

      if (Number.isFinite(valueInput)) {
        return valueInput
      } else {
        return 0
      }
    }

    /////////////////////// LISTENERS/DOM-RELATED FUNCTIONS
    document.getElementById('text-input').addEventListener('input', function () {
        const newLength = returnNumberOfWords(this)

        if (currentLength != newLength) {
            currentLength = newLength
            document.getElementById('nb-of-words').textContent = newLength;
        }
    });

    window.onclick = function(event) {
        if (
            modalDialog.contains(event.target) &&
            modalDialog.open == true &&
            !document.getElementById("timer-dialog-content").contains(event.target)
          ) {
          modalDialog.close()
          document.getElementById("timer-dialog-content").textContent = ""
        }
    }

    function changeMode(modeName) {
      let layout = document.getElementById("rich-text-editor-block")
      layout.classList.remove(layout.classList[0])
      layout.classList.add(modeName)
    }

    function playAudio(audioId) {
      let audioFile = document.getElementById(audioId); 
      audioFile.play()
    }