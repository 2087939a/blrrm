		var dataArray = [20,40,50, 60, 5];
		var width = 800;
		var height = 600;
		
		var widthScale = d3.scale.linear()
							.domain([0,60])
							.range([0,width]);
		
		
		
		var axis = d3.svg.axis()
						.scale(widthScale);
		
		var colorScale = d3.scale.linear()
							.domain([0,60])
							.range(["red","blue"]);
		
		var canvas = d3.select("#main")
						.append("svg")
						.attr("width", width)
						.attr("height", height)
						.append("g")
						.attr("transform", "translate(20, 0)");
						
		var bars = canvas.selectAll("rect")
						.data(dataArray)
						.enter()
							.append("rect")
							.attr("width", function(d) { return widthScale(d);})
							.attr("height",50)
							.attr("fill", function (d){ return colorScale(d);})
							.attr("y", function(d, i) { return i *100});
		canvas.append("g")
				.attr("transform","translate(0, 500)")
				.call(axis)
		console.log(d3);
