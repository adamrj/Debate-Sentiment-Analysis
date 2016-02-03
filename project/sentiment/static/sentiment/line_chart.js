


$( document ).ready(function() {
	
	$.getJSON("/sentiment/line_chart", function(result) {

		var all_candidates = {}
		
		for (candidate in result['candidates']) {
			var candidateData = [];
			for (k in result['candidates'][candidate]){
				candidateData.push({"minute": k, "score": result['candidates'][candidate][k]})
			}
			all_candidates[candidate] = candidateData
		}

	  var vis = d3.select("#visualisation"),
	    WIDTH = 1000,
	    HEIGHT = 500,
	    MARGINS = {
	        top: 20,
	        right: 20,
	        bottom: 20,
	        left: 50
    },

    xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([40,195]);

    yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([0,1]);

    xAxis = d3.svg.axis()
    .scale(xScale);
  
		yAxis = d3.svg.axis()
    .scale(yScale)
    .orient("left");

    vis.append("svg:g")
    .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
    .call(xAxis);

    vis.append("svg:g")
    .attr("transform", "translate(" + (MARGINS.left) + ",0)")
    .call(yAxis);

    var lineGen = d3.svg.line()
  	.x(function(d) {
    	return xScale(d.minute);
  	})
  	.y(function(d) {
    	return yScale(d.score);
  	}).interpolate("basis");

	  var colors = {"Trump": "red", "Bush": "purple", "Walker": "black", "Huckabee": "yellow", "Carson": "blue", "Cruz": "grey", "Rubio": "orange", "Paul": "brown", "Christie": "pink", "Kasich": "green"}

	  for (candidate in all_candidates) {
		  vis.append('svg:path')
		  .attr('class', candidate)
		  .attr('d', lineGen(all_candidates[candidate]))
		  .attr('stroke', colors[candidate])
		  .attr('stroke-width', 2)
		  .attr('fill', "transparent");
	  }

		$("path").click(function(event) {
			var candidate = $(this).attr("class")
			var xCoord = event['offsetX']
			var time = xCoord / 1000 * 155 + 40
			console.log(time)
			var rating = result['candidates'][candidate][parseInt(time)]
			console.log(rating)
			$.getJSON("/sentiment/tweet", {"time": time, "candidate": candidate, "rating": rating}, function(data) {
				console.log(data)
                $("#tweet").empty().append("<p>" + data.tweet + "</p>")
			})

		})

		

		$("path").on("mouseover", function() {
        d3.select(this)
          .attr("opacity", "0.5");
		});


		$("path").on("mouseout", function() {
        d3.select(this)
          .attr("opacity", "1");
		});

		$(".candidate_buttons").on("click", function() {
		var ID = $(this).attr("id")
		$("."+ID).toggle()
	})


	})
	
	




});
















	