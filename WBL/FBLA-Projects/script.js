fetch("projects.json")
    .then(response => response.json())
    .then(data => {

        const modalTitle = document.getElementById("projectModalTitle");
        const modalBody = document.getElementById("projectModalBody");

        const copyButton = document.getElementById("copyProject");
        const pdfButton = document.getElementById("savePdf");

        const allProjects = [
            ...data.codingProjects,
            ...data.businessMarketingEntrepreneurship,
            ...data.graphicDesign
        ];

        const buttons = document.querySelectorAll(".project-button");

        buttons.forEach(button => {
            button.addEventListener("click", () => {

                const projectName = button.dataset.project;

                const project = allProjects.find(
                    item => item.name === projectName
                );

                modalTitle.textContent = project.name;

                modalBody.innerHTML = project.description;

                const modal = new bootstrap.Modal(
                    document.getElementById("projectModal")
                );

                modal.show();
            });
            copyButton.addEventListener("click", () => {

                const textToCopy =
                    modalTitle.textContent +
                    "\n\n" +
                    modalBody.innerText;

                navigator.clipboard.writeText(textToCopy)
                    .then(() => {
                        copyButton.textContent = "Copied!";

                        setTimeout(() => {
                            copyButton.textContent = "Copy";
                        }, 1500);
                    });
            });

            pdfButton.addEventListener("click", () => {

                const printWindow = window.open("", "_blank");

                printWindow.document.write(`
        <!DOCTYPE html>
        <html>
        <head>
            <title>${modalTitle.textContent}</title>

            <style>
                body {
                    font-family: Arial, Helvetica, sans-serif;
                    margin: 40px;
                    color: #000033;
                }

                h1 {
                    font-size: 24px;
                    margin-bottom: 24px;
                }

                p {
                    line-height: 1.6;
                }
            </style>
        </head>

        <body>
            <h1>${modalTitle.textContent}</h1>

            ${modalBody.innerHTML}
        </body>
        </html>
    `);

                printWindow.document.close();

                printWindow.onload = () => {
                    printWindow.print();
                };
            });
        });
    });