
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

    var typage = document.getElementById("thankyou")
    typage.style.display = "none";

}

function set_display_ty() {
    reset_display()

    var typage = document.getElementById("thankyou")
    typage.style.display = "inline";
}

function ValidateInputs() {
    const fname = document.getElementById("name").value
    const age = document.getElementById("age").value
    const email = document.getElementById("email").value
    const phone = document.getElementById("phone").value
    const elidType = document.getElementById("id-type")
    var idType = elidType.options[elidType.selectedIndex].text

    const idNum = document.getElementById("id-num").value
    const street = document.getElementById("street").value
    const elstate = document.getElementById("state")
    var state = elstate.options[elstate.selectedIndex].text

    const zip = document.getElementById("zip").value
    var time
    const day = document.getElementById("day").value
    var marketing
    const comments = document.getElementById("comments").value

    var times = document.getElementsByName('time');
    for (i = 0; i < times.length; i++) {
        if (times[i].checked)
            time = times[i].value;
    }

    var markets = document.getElementsByName('marketing');
    for (i = 0; i < markets.length; i++) {
        if (markets[i].checked)
            marketing = markets[i].value;
    }

    let nameRE = /^([^0-9]*)$/
    let ageRE = /^[0-9][0-9]?$/
    let emailRE = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}$/
    let phoneRE = /^\d{3}-\d{3}-\d{4}$/
    let zipRE = /^\d{5}$/

    if(nameRE.test(fname)) {
        nready = true
        // console.log(fname)
    }else {
        nready = false
        alert("Name cannot contain numbers")
    }

    if(ageRE.test(age)) {
        aready = true
        // console.log(age)
    }else {
        aready = false
        alert("Age must be a number between 1 and 99")
    }

    if(emailRE.test(email)) {
        eready = true
        // console.log(fname)
    }else {
        eready = false
        alert("Email must be written in the format xxx@xxx.xxx")
    }

    if(phoneRE.test(phone)) {
        pready = true
        // console.log(fname)
    }else {
        pready = false
        alert("Phone must be in the format ###-###-####")
    }

    if(zipRE.test(zip)) {
        zready = true
        // console.log(fname)
    }else {
        zready = false
        alert("Zip must be 5 numbers only")
    }


    result = [fname, age, email, phone, idType, idNum, street, state, zip, time, day, marketing, comments]
    if ((((nready && aready)&& eready) && pready) && zready) {
        set_display_ty()
        console.log(result)
    }
    event.preventDefault();
}
