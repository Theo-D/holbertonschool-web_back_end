export default function createReportObject(employeesList) {
  const object = {
    allEmployees: employeesList,
    getNumberOfDepartments: (departments) => {return Object.keys(departments).length;}
  };

  return object;
}
