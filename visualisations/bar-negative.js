/*
<script src="https://code.highcharts.com/highcharts.js"></script>
<script src="https://code.highcharts.com/modules/exporting.js"></script>
*/

// http://jsfiddle.net/vdwprmsL/

Highcharts.chart('container0', {
  chart: {
    type: 'bar'
  },
  title: {
    text: 'Percentage change in number of deaths between 2003-2013'
  },
  xAxis: {
    categories: ['All Causes', "Alzheimer's disease", 'Cancer', 'Chronic liver 						disease and cirrhosis', 'Chronic lower respiratory disease', 'Diabetes', 'Diseases of Heart', 'Essential hypertension and hypertensive renal disease', 'Homicide', 'Influenza and pneumonia', 'Kidney Disease', "Parkinson's disease", 'Pneumonitis due to solids and liquids', 'Septicemia', 'Stroke', 'Suicide', 'Unintentional Injuries']
  },
  credits: {
    enabled: false
  },
  series: [{
    name: 'Percentage change',
    data: [5.73, 25.14, 4.78, 24.5, 15.3, 1.8, -12.11, 28.7, -9.99, -14.36,
    9.89, 28.57, 6.7, 10.71, -22.26, 23.49, 16.3]
  }]
});
