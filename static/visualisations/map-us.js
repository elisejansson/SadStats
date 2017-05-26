
$.getJSON("C:/Users/ASUS/Documents/Uni/2017/2017 SEMESTER 1/Foundations of Informatics/Project/Phase 3/SadStats/static/visualisations/highcharts-us-data.json", function (data) {

    // Make codes uppercase to match the map data
    $.each(data, function () {
        this.code = this.code.toUpperCase();
    });

    // var data = [
    //     ['AL', 962.0],
    //     ['AK', 766.4],
    //     ['AZ', 727.4],
    //     ['AR', 911.4],
    //     ['CA', 684.1],
    //     ['CO', 709.0],
    //     ['CT', 682.4],
    //     ['DE', 790.2],
    //     ['DC', 871.5],
    //     ['FL', 719.9],
    //     ['GA', 867.1],
    //     ['HI', 620.0],
    //     ['ID', 750.8],
    //     ['IL', 772.9],
    //     ['IN', 844.0],
    //     ['IA', 735.8],
    //     ['KS', 785.0],
    //     ['KY', 927.7],
    //     ['LA', 942.3],
    //     ['ME', 774.2],
    //     ['MD', 770.0],
    //     ['MA', 707.8],
    //     ['MI', 807.2],
    //     ['MN', 673.2],
    //     ['MS', 980.3],
    //     ['MO', 842.6],
    //     ['MT', 776.5],
    //     ['NE', 739.6],
    //     ['NV', 832.7],
    //     ['NH', 723.1],
    //     ['NJ', 724.6],
    //     ['NM', 773.0],
    //     ['NY', 697.3],
    //     ['NC', 831.5],
    //     ['ND', 712.5],
    //     ['OH', 840.7],
    //     ['OK', 935.5],
    //     ['OR', 752.1],
    //     ['PA', 798.6],
    //     ['RI', 738.3],
    //     ['SC', 875.0],
    //     ['SD', 731.9],
    //     ['TN', 914.6],
    //     ['TX', 795.3],
    //     ['UT', 725.3],
    //     ['VT', 726.2],
    //     ['VA', 776.9],
    //     ['WA', 722.5],
    //     ['WV', 955.0],
    //     ['WI', 735.2],
    //     ['WY', 787.1],
    // ];
    // Instanciate the map
    Highcharts.mapChart('container3', {

        chart: {
            borderWidth: 1
        },

        title: {
            text: 'US population density (/km²)'
        },

        legend: {
            layout: 'horizontal',
            borderWidth: 0,
            backgroundColor: 'rgba(255,255,255,0.85)',
            floating: true,
            verticalAlign: 'top',
            y: 25
        },

        mapNavigation: {
            enabled: true
        },

        colorAxis: {
            min: 1,
            type: 'logarithmic',
            minColor: '#EEEEFF',
            maxColor: '#000022',
            stops: [
                [0, '#EFEFFF'],
                [0.67, '#4444FF'],
                [1, '#000022']
            ]
        },

        series: [{
            animation: {
                duration: 1000
            },
            data: data,
            mapData: Highcharts.maps['countries/us/us-all'],
            joinBy: ['postal-code', 'code'],
            dataLabels: {
                enabled: true,
                color: '#FFFFFF',
                format: '{point.code}'
            },
            name: 'Population density',
            tooltip: {
                pointFormat: '{point.code}: {point.value}/km²'
            }
        }]
    });
});
