function load_lesson(lesson) {
    if (lesson) {
        console.log(lesson)
        window.location.href = "/lessons/" + encodeURIComponent(lesson)
    }
    else {
        console.log("No lesson selected")
    }
}