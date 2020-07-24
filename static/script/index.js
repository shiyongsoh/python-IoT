var linestatsCall = 0; //this is to count how many times the line graph is called
window.onload = function() {
    var ctx = document.getElementById('myChart').getContext('2d');
    window.myLine = new Chart(ctx, config);
};

function dataAnalytics(data){
    document.createElement()
}


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
