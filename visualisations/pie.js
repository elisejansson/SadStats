/*
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/highcharts-3d.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>

<div id="container" style="height: 400px"></div>
*/

// http://jsfiddle.net/vps8kp8s/

Highcharts.setOptions({
 colors: ['	#D1382F', '#F37736','#FFEC50', '#7BC043','#0392CF','#D3D3D3']
});
Highcharts.chart('container2', {
    chart: {
        type: 'pie',
        options3d: {
            enabled: true,
            alpha: 45,
            beta: 0
        }
    },
    title: {
        text: 'Top 5 Causes of Death in the US, 2003-2013'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            depth: 35,
            dataLabels: {
                enabled: true,
                format: '{point.name}'
            }
        }
    },
    series: [{
        type: 'pie',
        name: 'percentage of all deaths',
        data: [
        		{
            		name: 'Diseases of Heart',
              	y: 25.24,
              	sliced: true,
              	selected: true,
              },
            ['Cancer', 22.98],
            ['Stroke', 5.53],
            ['Chronic lower respiratory disease', 5.46],
            ['Unintentional Injuries', 4.89],
            ['All other causes', 35.9]
        ]
    }]
});
