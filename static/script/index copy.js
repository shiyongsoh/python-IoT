var linestatsCall = 0; //this is to count how many times the line graph is called

function dataAnalytics(data){
    document.createElement()
}

function lineGraph(color,data,label,elementName,time){
    if(linestatsCall > 0){
        data = `data${linestatsCall}`
    }
    console.log(data)
    console.log(color)
    console.log(label)
    console.log(elementName)
    var ctx = document.getElementById("chart").getContext('2d');
    var config = {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'My First dataset',
                backgroundColor: "#ff0000",
                borderColor: "#ff0000",
                data: ['23', '24', '25', '23', '21', '22', '24', '26', '27', '26'],
                fill: false,
            }, {
                label: 'My Second dataset',
                fill: false,
                backgroundColor: "#ffff00",
                borderColor: "#ffff00",
                data: ['55', '57', '60', '59', '62', '66', '70', '68', '66', '65'],
            }]
        },
        options: {
            responsive: true,
            title: {
                display: true,
                text: 'Chart.js Line Chart'
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Month'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Value'
                    }
                }]
            }
        }
    };
    return linestatsCall ++
}
            window.onload = function() {
                var ctx = document.getElementById('myChart').getContext('2d');
                window.myLine = new Chart(ctx, config);
            };

function addData(chart, label, data) {
    chart.data.labels.push(label);
    chart.data.datasets.forEach((dataset) => {
        dataset.data.push(data);
    });
    chart.update();
}

function removeData(chart) {
    chart.data.labels.pop();
    chart.data.datasets.forEach((dataset) => {
        dataset.data.pop();
    });
    chart.update();
}

//showing data to graph

function showData(data){
    // var JSONObject = JSON.parse(data);)
    console.log(data)
    //  console.log(typeof(data.weather[0]))
    //  console.log(data.weather[0])
    //lineGraph("#91fff8",data,"hmm","myChart")     
    return data
}

function asdf(){
    $("#button").append("hmm")
    console.log("this is clicked")
}
