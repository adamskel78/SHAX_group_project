const inputs = {}

function updateInputs() {
    
    let input = d3.select(this)

    let value = input.property("value").trim();

    let id = input.attr("id");

    inputs[id] = parseInt(value, 10)
    
    console.log(inputs)
}


function submitData() {
      d3.json('/predict', {
      method:"POST",
      body: JSON.stringify(
        inputs
      ),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(res => {
      d3.select("#results").text(res.Probability)
    });

    d3.json('/predict', {
      method:"POST",
      body: JSON.stringify(
        inputs
      ),
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    })
    .then(res => {
      console.log(res)
      d3.select("#suggestion").text(res.Suggestions)
    });
}

function optionChanged() {
  // add a button
  // onlicke listener on the button
  // generate a random number 0-1000 
  const randomNumber = Math.floor(Math.random() * 70000);
  // to make that call (to your app route) using that random number
  d3.json(`/record/${randomNumber}`).then((data) => {
    var resultArray = data.filter(sampleObj => sampleObj.id == randomNumber);
    console.log(resultArray);
    var result = resultArray[0];
    // console.log(result);
    var PANEL = d3.select("#sample-metadata");

    PANEL.html("");
    Object.entries(result).forEach(([key,value]) => {
      PANEL.append("h5").text(key+": " + value);
    });


  var level = 200*result.prob;

      // Trig to calc meter point
      var degrees = 180 - level,
          radius = .5;
      var radians = degrees * Math.PI / 180;
      var x = radius * Math.cos(radians);
      var y = radius * Math.sin(radians);
      var path1 = (degrees < 45 || degrees > 135) ? 'M -0.0 -0.025 L 0.0 0.025 L ' : 'M -0.025 -0.0 L 0.025 0.0 L ';
      // Path: may have to change to create a better triangle
      var mainPath = path1,
          pathX = String(x),
          space = ' ',
          pathY = String(y),
          pathEnd = ' Z';
      var path = mainPath.concat(pathX,space,pathY,pathEnd);

      var data = [{ type: 'scatter',
        x: [0], y:[0],
          marker: {size: 14, 
            color:'850000',
            colorscale:'YlGnBu'},
          showlegend: false,
          name: 'speed',
          text: level,
          hoverinfo: 'text+name'},
        { values: [1,1,1,3],
        rotation: 90,
        text: ['high', 'medium','low',''],
        textinfo: 'text',
        textposition:'inside',
        marker: {
          colors: [
            "rgba(255, 99, 71, .5)",
            "rgba(255, 165, 0, .5)",
            "rgba(14, 127, 199, .5)",
            "rgba(255, 255, 255, 0)"
          ]
        },
        hoverinfo: 'label',
        hole: .5,
        type: 'pie',
        showlegend: false
      }];

      var layout = {
        shapes:[{
            type: 'path',
            path: path,
            fillcolor: '850000',
            line: {
              color: '850000'
            }
          }],
        height: 400,
        width: 400,
        title: '<b>'+'Object Probability of Cardiovascular Disease'+ '</b>',
        xaxis: {zeroline:false, showticklabels:false,
                  showgrid: false, range: [-1, 1]},
        yaxis: {zeroline:false, showticklabels:false,
                  showgrid: false, range: [-1, 1]}
      };

      Plotly.newPlot('gauge', data, layout);

  });

}

optionChanged()

// Attach an event to listen for changes to each filter
// Hint: You'll need to select the event and what it is listening for within each set of parenthesis
d3.selectAll("input").on("change", updateInputs);

d3.select('#submit-btn').on('click', submitData)
d3.select('#filter-btn').on('click', optionChanged)