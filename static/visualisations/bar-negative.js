Highcharts.chart('container0', {
  chart: {
    borderColor: 'grey',
    borderRadius: 20,
    borderWidth: 1,
    marginRight: 40,
    type: 'bar',
    borderRadius: '25px'
  },
  title: {
    text: 'Percentage change in number of deaths between 2003-2013'
  },
  xAxis: {
    categories: ['All Causes', "Alzheimer's disease", 'Cancer', 'Chronic liver disease and cirrhosis', 'Chronic lower respiratory disease', 'Diabetes', 'Diseases of Heart', 'Essential hypertension and hypertensive renal disease', 'Homicide', 'Influenza and pneumonia', 'Kidney Disease', "Parkinson's disease", 'Pneumonitis due to solids and liquids', 'Septicemia', 'Stroke', 'Suicide', 'Unintentional Injuries'],
    title: {
        text: 'Cause'
    }
},
  yAxis: {
    title: {
        text: 'Percentage',
        align: 'middle'
    }

  },
  credits: {
    enabled: false
  },
  series: [{
    name: 'Percentage change',
    color: '#D1382F',
    negativeColor: '#0392CF',

    data: [5.73, 25.14, 4.78, 24.5, 15.3, 1.8, -12.11, 28.7, -9.99, -14.36,
    9.89, 28.57, 6.7, 10.71, -22.26, 23.49, 16.3]
  }]
});
