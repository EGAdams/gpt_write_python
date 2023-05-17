            'Pull vertical columns out of large "A" and small adjustments to it as well.',
            'Small change of large "d".',
            'Adjustments for smaller fonts "5" and "6".'
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

document.getElementById('printButton').addEventListener('click', function() {
    window.print();
});