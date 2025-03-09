

function schedule_booking() {
    console.log("name")
    var name = document.getElementById('name').value;
    var age = document.getElementById('age').value;
    var idType = document.getElementById('id-type').value;
    var idNum = document.getElementById('id-num').value;
    var day = document.getElementById('day').value;
    var time;
    var times = document.getElementsByName('time');
    for (i = 0; i < times.length; i++) {
        if (times[i].checked)
            time = times[i].value;
    }

    let booking = {
        Bname: name,
        Bage: age,
        BidType: idType,
        BidNum: idNum,
        Bday: day,
        Btime: time
    }

    alert("Welcome " + name + ", we look forward to seeing you on " + day)
}
