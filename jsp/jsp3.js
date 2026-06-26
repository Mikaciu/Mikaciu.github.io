const JSP3_COLOR = "#f28a15";

const JSP3_DATES_BLACKLIST = [];

const JSP3_DATES = LESSONS_DATES.filter(
  (date) => !JSP3_DATES_BLACKLIST.includes(date),
);

const JSP3_LESSONS = [
    ["INC-A1", "SC-A1"], ["INC-B1", "SC-B1"]
];

const JSP3_EVENTS = [
  ...JSP3_DATES.map((date, index) => {
    const content = JSP3_LESSONS[index] || [];
    return {
      title: `JSP 3 - cours ${index + 1}`,
      start: `${date}T08:00:00`,
      color: JSP3_COLOR,
      extendedProps: {
        content: content.map((lesson) => JSP3_CONTENT[lesson]),
      },
    };
  }),
  ...["2026-09-12", "2026-09-19", "2026-09-26", "2026-10-03", "2026-10-10"].map(
    (date) => {
      return {
        title: "🩺 JSP3 SAP - M1",
        start: `${date}T08:00:00`,
        end: `${date}T08:00:00`,

        color: JSP3_COLOR,
        extendedProps: {
          location: "CS Belfort Nord",
        },
      };
    },
  ),
  {
    title: "🔥 JSP3 INC",
    start: "2026-10-26T08:00:00",
    end: "2026-10-31T17:00:00",

    color: JSP3_COLOR,
    extendedProps: {
      location: "CS Delle",
    },
  },
];
