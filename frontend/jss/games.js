var del = $(".delete")
del.click(function (event) {
    var id = parseInt(event.target.parentElement.pathname.split("games/")[1])
    $.ajax({
        type: "DELETE",
        url: `/games/${id}`,
        success: function (response) {
            console.log(response)
        }
    })
})
var highScores = $(".high-scores")
highScores.click(function () {
    fetch('/highscores', { method: "GET", redirect: 'follow' })
        .then(function (response) {
            window.location = response.url
        })
})
var gamesBack = $(".hg-scr-back")
gamesBack.click(function () {
    fetch('/games', { method: "GET", redirect: 'follow' })
        .then(function (response) {
            window.location = response.url
        })
})