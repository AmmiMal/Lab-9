function addPortfolio() {
    let projName = document.getElementById('title').value
    let link = document.getElementById('link').value
    fetch('/add', {
        method: 'post',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({'title': projName,
                             'link': link})
    })}

function clearNotes() {
    document.getElementById("output_clear").innerHTML = ""
    fetch('/clear', {
        method: 'post',
        })}