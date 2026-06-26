const JSP4_COLOR = "#0b8236";

const JSP4_DATES_BLACKLIST = [];

const JSP4_DATES = LESSONS_DATES.filter(
  (date) => !JSP4_DATES_BLACKLIST.includes(date),
);

const JSP4_LESSONS = [[], []];

const JSP4_EVENTS = [
  ...JSP4_DATES.map((date, index) => {
    const content = JSP4_LESSONS[index] || [];
    return {
      title: `JSP 4 - cours ${index + 1}`,
      start: `${date}T08:00:00`,
      color: JSP4_COLOR,
      extendedProps: {
        content: content.map((lesson) => JSP4_CONTENT[lesson]),
      },
    };
  }),
  ...[
    "2026-08-29",
    "2026-09-05",
    "2026-09-12",
    "2026-09-19",
    "2026-09-26",
    "2026-10-03",
    "2026-10-10",
    "2026-10-17",
  ].map((date) => {
    return {
      title: "🔥 JSP4 INC",
      start: `${date}T08:00:00`,
      end: `${date}T08:00:00`,

      color: JSP4_COLOR,
      extendedProps: {
        location: "CS Delle",
      },
    };
  }),
  {
    title: "🔥 JSP4 INC",
    start: "2026-10-19T08:00:00",
    end: "2026-10-24T17:00:00",

    color: JSP4_COLOR,
    extendedProps: {
      location: "CS Delle",
    },
  },
  ...[
    "2026-10-31",
    "2026-11-07",
    "2026-11-21",
    "2026-11-28",
    "2026-12-05",
    "2026-12-12",
  ].map((date) => {
    return {
      title: "🩺 JSP4 SAP - M2",
      start: `${date}T08:00:00`,
      end: `${date}T08:00:00`,

      color: JSP4_COLOR,
      extendedProps: {
        location: "CS Belfort Nord",
      },
    };
  }),
];
