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

window.addEventListener("load", function () {
    var openGames = document.getElementsByClassName("game shadowed");
    for (var l = 0; l < openGames.length; l++) {
        if (openGames[l].classList.contains("open")) {
            console.log("open");
        } else {
            openGames[l].classList.add("hide-game");
        }
    }
});

var filters = document.getElementsByClassName("filter clickable");
for (var i = 0; i < filters.length; i++) {
    filters[i].addEventListener("click", function (e) {
        var filterButtons = document.getElementsByClassName("filter clickable");
        for (var k = 0; k < filters.length; k++) {
            if (filterButtons[k].classList.contains("filter-selected")) {
                filterButtons[k].classList.remove("filter-selected");
            }
        }
        e.target.classList.toggle("filter-selected");
        var allGames = document.getElementsByClassName("game shadowed");
        var currentFilter = e.target.textContent.toLowerCase();
        for (var j = 0; j < allGames.length; j++) {
            if (currentFilter == "all") {
                allGames[j].classList.remove("hide-game")
            } else if (allGames[j].classList.contains(currentFilter)) {
                allGames[j].classList.remove("hide-game")
            } else {
                allGames[j].classList.add("hide-game")
            }
        }
    })
}