


$( document ).ready(function() {
	
	$.getJSON("/sentiment/dot_chart", function(result) {
		var all_tweets = result["all_tweets"]
		// time, score, text, ,candidate
		var dataset = []
		console.log(all_tweets[0]['time'])
		console.log(all_tweets[0]['score'])
		console.log(all_tweets[0]['text'])
		console.log(all_tweets[0]['candidate'])

		for (tweet in all_tweets) {
			var time = all_tweets[tweet]['time']
			var score = all_tweets[tweet]['score']
			var text = all_tweets[tweet]['text']
			var candidate = all_tweets[tweet]['candidate']
			dataset.push([time,score,text,candidate])
		}


	//Width and height
	var w = 1200;
	var h = 500;
	
	//Create scale functions
	var xScale = d3.scale.linear()
						 .domain([0, d3.max(dataset, function(d) { return d[0]; })])
						 .range([0, w]);
	

	var yScale = d3.scale.linear()
						 .domain([0, d3.max(dataset, function(d) { return d[1]; })])
						 .range([0, h]);

	//Create SVG element
	var svg = d3.select("body")
				.append("svg")
				.attr("width", w)
				.attr("height", h);

	var colors = {"Trump": "red", "Bush": "purple", "Walker": "black", "Huckabee": "yellow", "Carson": "blue", "Cruz": "grey", "Rubio": "orange", "Paul": "brown", "Christie": "pink", "Kasich": "green"}

	svg.selectAll("circle")
	   .data(dataset)
	   .enter()
	   .append("circle")
	   .attr("cx", function(d) {
	   		return xScale(d[0]);
	   })
	   .attr("cy", function(d) {
	   		return h- yScale(d[1]);
	   })
	   .attr("r", function(d) {
	   		return 3;
	   })
	   .attr("fill",function(d) {
	   		return colors[d[3]]
	   })
	   .on("mouseover",function() {
	   	d3.select(this).attr("r","30")
	   })
	   .on("mouseout",function() {
	   	d3.select(this).attr("r","3")
	   })
	   .on("click",function(d) {
	   	var candidate = d[3]
	   	var tweet = d[2]
	   	var score = d[1]
	   	$("#tweet").html("<p>"+candidate+"</p> <p>" + tweet + "</p> <p>" + score + "</p>")
	   })


	   ;



	// svg.selectAll("text")
	//    .data(dataset)
	//    .enter()
	//    .append("text")
	//    .text(function(d) {
	//    		return d[0] + "," + d[1];
	//    })
	//    .attr("x", function(d) {
	//    		return xScale(d[0]);
	//    })
	//    .attr("y", function(d) {
	//    		return yScale(d[1]);
	//    })
	//    .attr("font-family", "sans-serif")
	//    .attr("font-size", "11px")
	//    .attr("fill", "red");
	




	})
	
	


});

