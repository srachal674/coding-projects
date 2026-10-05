fetch("projects.json")
    .then(response => response.json())
    .then(data => {

        const modalTitle = document.getElementById("projectModalTitle");
        const modalBody = document.getElementById("projectModalBody");

        const copyButton = document.getElementById("copyProject");
        const pdfButton = document.getElementById("savePdf");

        const guidelinesSection = document.createElement("p");

        const guidelinesLink = document.createElement("a");
        guidelinesLink.href = project.eventUrl;
        guidelinesLink.target = "_blank";
        guidelinesLink.rel = "noopener noreferrer";
        guidelinesLink.textContent = "official FBLA Event Details & Guidelines";

        guidelinesSection.append("Use the ");
        guidelinesSection.appendChild(guidelinesLink);
        guidelinesSection.append(
            " to create your requirements checklist in your README."
        );

        modalBody.appendChild(guidelinesSection);
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
        });        
    });