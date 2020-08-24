const inputs = {
    active: 1,
    age: 50,
    alco: 0,
    ap_hi: 50,
    ap_lo: 10,
    cholesterol: 1,
    gender: 2,
    gluc: 1,
    height: 185,
    smoke: 0,
    weight: 80
    }

function updateInputs() {
    
    let input = d3.select(this)

    let value = input.property("value").trim();

    let id = input.attr("id");

    inputs[id] = parseInt(value, 10)
    
    console.log(inputs)
}


function submitData() {
    console.log("Hi")
    return d3.json('/predict', {
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
      d3.select("#result").text(res.Probability)
    });
}


function buildMetadata(sample) {
  console.log("Here")
  d3.json("/demo").then((data) => {
    var metadata = data.age;
    var resultArray = metadata.filter(sampleObj => sampleObj.id == sample);
    console.log(resultArray);
    var result = resultArray[0];
    console.log(result);
    var PANEL = d3.select("#sample-metadata");

    PANEL.html("");
    Object.entries(result).forEach(([key,value]) => {
      PANEL.append("h6").text(key+": " + value);
    });
  });
}



// Attach an event to listen for changes to each filter
// Hint: You'll need to select the event and what it is listening for within each set of parenthesis
d3.selectAll("input").on("change", updateInputs);

d3.select('#filter-btn').on('click', submitData)