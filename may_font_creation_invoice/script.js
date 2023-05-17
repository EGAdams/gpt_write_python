// Raw data
// Raw data
const rawData = [
    {
        date: '4-29',
        tasks: [
            'Create large characters "|", "15", "30", "1", "2", "6", "8", "9" and "0".',
            'Created numbers in smaller fonts: "6", "4", "8", "6", "1".'
        ],
        hours: 5.0
    },
    {
        date: '5-1',
        tasks: [
            'Refine large fonts "9", "8", "6", "4", "2"',
            'Tweaking "0" and "3".'
        ],
        hours: 7.5
    },
    {
        date: '5-2',
        tasks: [
            'Create and tweak "Ad" characters.'
        ],
        hours: 3.0
    },
    {
        date: '5-3',
        tasks: [
            'Adjust "3" and "5".',
            'Tweak spaces between large and small characters'
        ],
        hours: 3.0
    },
    {
        date: '5-4',
        tasks: [
            'Fipped "6" and made adjustments for new "9".',
            'Adjust pixels for "8" and add new column.'
        ],
        hours: 2.5
    },
    {
        date: '5-5',
        tasks: [
            'Fix little fonts "5" and "6".',
            'Finished adjusting pixels for "9".',
            'Created large "7"'
        ],
        hours: 1.5
    },
    {
        date: '5-6',
        tasks: [
            'Pull vertical columns out of large "A" and small adustments to it as well.',
            'Small change of large "d".',
            'Adjustments for smaller fints "5" and "6".'
        ],
        hours: 3.5
    },
    {
        date: '5-8',
        tasks: [
            'Finish remaining adjustments for "d"',
            'Finish remaining adjustments for large fonts "5", "6" and "9".',
            'Finish remaining adjustments for small fonts "5" and "6".'
        ],
        hours: 2.5
    }
];

// Hourly rate
const hourlyRate = 25;

// Calculate total cost
let totalCost = 0;
rawData.forEach(item => {
    totalCost += item.hours * hourlyRate;
});

// Populate invoice
const invoiceDiv = document.getElementById('invoiceData');
rawData.forEach(item => {
    const row = document.createElement('tr');

    const dateCell = document.createElement('td');
    dateCell.textContent = item.date;
    row.appendChild(dateCell);

    const tasksCell = document.createElement('td');
    tasksCell.textContent = item.tasks.join(', ');
    row.appendChild(tasksCell);

    const hoursCell = document.createElement('td');
    hoursCell.textContent = item.hours;
    row.appendChild(hoursCell);

    const costCell = document.createElement('td');
    costCell.textContent = `$${item.hours * hourlyRate}`;
    row.appendChild(costCell);

    invoiceDiv.appendChild(row);
});

const totalRow = document.createElement('tr');
totalRow.classList.add('total_row');

const totalCell = document.createElement('td');
totalCell.textContent = 'Total';
totalCell.colSpan = 3;
totalRow.appendChild(totalCell);

const totalCostCell = document.createElement('td');
totalCostCell.textContent = `$${totalCost}`;
totalCostCell.classList.add('total');
totalRow.appendChild(totalCostCell);

invoiceDiv.appendChild(totalRow);

document.getElementById('invoiceDate').textContent = new Date().toLocaleDateString();

document.getElementById('printButton').addEventListener('click', function() {
    window.print();
});