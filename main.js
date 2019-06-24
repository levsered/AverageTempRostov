function get_avr_temp()
{
    var myRequest = new Request('score');
    fetch(myRequest).then(function (res) {
        res.json().then(function (data) {
            console.log(data);
            var div = document.querySelector("#c01");
            div.innerHTML = data["average"][0] + " °С ";
            var div = document.querySelector("#c02");
            div.innerHTML = data["average"][1] + " °С ";
            var div = document.querySelector("#c03");
            div.innerHTML = data["average"][2] + " °С ";
            var div = document.querySelector("#f01");
            div.setAttribute("src", data["weather_type"][0]);
            var div = document.querySelector("#f02");
            div.setAttribute("src", data["weather_type"][1]);
            var div = document.querySelector("#f03");
            div.setAttribute("src", data["weather_type"][2]);
        });
    });

}