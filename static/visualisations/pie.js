Highcharts.chart('container2', {
    chart: {
        borderColor: 'grey',
        borderRadius: 20,
        borderWidth: 1,
        marginTop: 1,
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

        colors: ['#D1382F', '#F37736','#FFEC50', '#7BC043','#0392CF','#D3D3D3'],

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
