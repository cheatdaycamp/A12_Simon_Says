var del = $(".delete")
del.click(function(event) {
    var id = parseInt(event.target.parentElement.pathname.split("games/")[1])
    $.ajax({
        type: "DELETE",
        url: `/games/${id}`,
        success: function(response) {
            console.log(response)
        }
    })
})