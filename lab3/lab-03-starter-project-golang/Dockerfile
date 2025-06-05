
FROM golang:1.19-alpine AS builder

WORKDIR /src/app 

COPY go.mod go.sum ./
RUN go mod download

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /app/main .

FROM gcr.io/distroless/static-debian12

WORKDIR /app

COPY --from=builder /app/main /app/main
COPY --from=builder /src/app/templates /app/templates/

EXPOSE 8080

CMD ["/app/main", "serve"]