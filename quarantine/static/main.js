$(document).ready(function (){
    $.getJSON("https://api.covid19india.org/data.json",function(data){
        var states = [];
        var confirmed = [];
        var recovered = [];
        var deaths = [];


        var total_active;
        var total_confirmed;
        var total_recovered;
        var total_deaths;

        total_active = data.statewise[0].active;
        total_confirmed = data.statewise[0].confirmed;
        total_recovered = data.statewise[0].recovered;
        total_deaths = data.statewise[0].deaths;

        //console.log(data.statewise);
        $.each(data.statewise, function (id, obj) {
            states.push(obj.state);
            confirmed.push(obj.confirmed);
            recovered.push(obj.recovered);
            deaths.push(obj.deaths);
          });
      // console.log(states);  
      
      states.shift();
      confirmed.shift();
      recovered.shift();
      deaths.shift();

      $("#confirmed").append(total_confirmed);
      $("#active").append(total_active);
      $("#recovered").append(total_recovered);
      $("#deaths").append(total_deaths);

      // Chart initialization
    var myChart = document.getElementById("myChart").getContext("2d");
  
      //console.log(states); 

      var chart = new Chart(myChart, {
        type: "bar",
        data: {
          labels: states,
          datasets: [
            {
              label: "Confirmed Cases",
              data: confirmed,
              backgroundColor: "#f1c40f",
              minBarLength: 50,
            },
            {
              label: "Recovered",
              data: recovered,
              backgroundColor: "#2ecc71",
              minBarLength: 40,
            },
            {
              label: "Deceased",
              data: deaths,
              backgroundColor: "#e74c3c",
              minBarLength: 20,
            },
          ],
        },
        option: {},
      });

    });

});