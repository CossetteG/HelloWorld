

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

function reset_display() {
    console.log("Setting new page")

    var homepage = document.getElementById("Home")
    homepage.style.display = "none";
    
    var rulespage = document.getElementById("Rules")
    rulespage.style.display = "none";

    var shpage = document.getElementById("schedule-housing")
    shpage.style.display = "none";

    var ompage = document.getElementById("our-mission")
    ompage.style.display = "none";

    var cupage = document.getElementById("contact-us")
    cupage.style.display = "none";

}

function set_display_home() {
    reset_display()

    var homepage = document.getElementById("Home")
    homepage.style.display = "inline";
}

function set_display_rules() {
    reset_display()

    var rulespage = document.getElementById("Rules")
    rulespage.style.display = "inline";
}

function set_display_sh() {
    reset_display()

    var shpage = document.getElementById("schedule-housing")
    shpage.style.display = "inline";

}

function set_display_om() {
    reset_display()

    var ompage = document.getElementById("our-mission")
    ompage.style.display = "inline";
}

function set_display_cu() {
    reset_display()

    var cupage = document.getElementById("contact-us")
    cupage.style.display = "inline";
}

var imgtoggle = true;

function toggle_dark() {
    console.log("going dark")

    document.querySelector("section").classList.toggle("dark-mode-c");
    document.querySelector("body").classList.toggle("dark-mode-c");
    document.querySelector("header").classList.toggle("dark-mode-h");
    document.querySelector("h1").classList.toggle("dark-mode-h");
    document.querySelector("footer").classList.toggle("dark-mode-f");
    document.querySelector("button").classList.toggle("dark-mode-f");

    var headings = document.querySelectorAll("h3");
    headings.forEach(element => {
        element.classList.toggle("dark-mode-f")
    });

    if (imgtoggle) {
        document.getElementById("darkmode").style.backgroundImage = 'url("img/toggle_light.png")';
        imgtoggle = false;
    } else {
        document.getElementById("darkmode").style.backgroundImage = 'url("img/toggle_dark.png")';
        imgtoggle = true;
    }
}