// http://jsfiddle.net/qdjhffcw/

Highcharts.chart('container1', {
  chart: {
    borderColor: 'grey',
    borderRadius: 20,
    borderWidth: 1,
    marginRight: 40,
    type: 'bar'
  },
  title: {
    text: 'Pecrentage Decrease in AADR from 2003-2013'
  },
  xAxis: {
    categories: ["District of Columbia", "California", "Maryland", "Colorado",
    "Nevada", "New Jersey", "Virginia", "Massachusetts", "New York", "Georgia",
    "Florida", "Arizona", "Delaware", "South Dakota", "Wyoming", "Illinois",
    "North Carolina", "Alaska", "Washington", "Texas", "Connecticut", "Oregon",
    "South Carolina", "New Mexico", "Pennsylvania", "New Hampshire",
    "Louisiana", "Hawaii", "Tennessee", "Rhode Island", "Missouri", "Utah",
    "Nebraska", "Idaho", "Ohio", "Minnesota", "Alabama", "Maine", "Montana",
    "Michigan", "Vermont", "Kentucky", "Kansas", "North Dakota",
    "West Virginia", "Indiana", "Wisconsin", "Oklahoma", "Mississippi", "Iowa",
    "Arkansas", "All states combined"],
    title: {
      text: 'State'
    }
  },
  yAxis: {
    min: 0,
    title: {
      text: 'Percentage',
      align: 'middle'
    },
    labels: {
      overflow: 'justify'
    }
  },
  tooltip: {
    valueSuffix: '%'
  },
  plotOptions: {
    bar: {
      dataLabels: {
        enabled: true
      }
    }
  },
  legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle',
    x: -40,
    y: 80,
    floating: true,
    borderWidth: 1,
    backgroundColor:
    ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
    shadow: true
  },
  credits: {
    enabled: false
  },
  series: [{
    name: 'Percentage decrease',
    data: [24.27, 18.00, 17.83, 17.25, 16.98, 16.27, 16.04, 15.87, 15.80,
    15.74, 15.67, 15.56, 14.78, 14.73, 14.69, 14.48, 14.46, 14.12, 13.93,
    13.12, 12.63, 12.17, 12.06, 12.05, 11.56, 11.49, 11.44, 11.44, 11.36,
    11.16, 10.95, 10.48, 10.46, 10.11, 9.72, 9.70, 9.31, 9.11, 9.11, 9.09,
    8.86, 8.77, 8.66, 8.56, 7.91, 7.76, 7.69, 7.68, 6.98, 6.76, 5.74, 12.13]
  }]
});
