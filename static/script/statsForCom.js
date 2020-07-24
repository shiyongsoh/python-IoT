var ctx2 = document.getElementById('myChart').getContext('2d');

// console.log(ctx)
var options = {
    backgroundColor : "#aa42f5",
    hoverBackgroundColor : "#8d42f5"
};


var data = {
    datasests:[{
        label:"com stats",
        data:[],
    }],
    label:[
        "Red",
        "Yellow"
    ]
}
var myPieChart = new Chart(ctx2, {
    type: 'pie',
    data: data,
    options: options
});


function showdata(data){
    console.log("showData is working")
    var newHTML = document.open("text/html","data");
    newHTML.write(data)
    newHTML.close()
    console.log(data)
}

console.log("This is running")