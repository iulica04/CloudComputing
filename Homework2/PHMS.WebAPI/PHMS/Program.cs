using Application;
using Domain.Services;
using Infrastructure;
using Infrastructure.Services;
using Microsoft.Extensions.Configuration;

var builder = WebApplication.CreateBuilder(args);

// CORS
var AllowAllOrigins = "AllowAllOrigins";
builder.Services.AddCors(options =>
{
    options.AddPolicy(name: AllowAllOrigins,
        policy =>
        {
            policy.AllowAnyOrigin();
            policy.AllowAnyHeader();
            policy.AllowAnyMethod();
        });
});

// Verifică dacă aplicația rulează în modul de testare
bool useInMemoryDatabaseEnvVar = builder.Configuration.GetValue<bool>("UseInMemoryDatabase");

// Adaugă serviciile pentru aplicație și infrastructură
builder.Services.AddApplication();
builder.Services.AddInfrastructure(builder.Configuration, useInMemoryDatabaseEnvVar);

// Adaugă HttpClient pentru MedicationExternalService
builder.Services.AddHttpClient<IMedicationExternalService, MedicationExternalService>(client =>
{
    client.BaseAddress = new Uri("http://localhost:8000");
});

builder.Services.AddSingleton<GoogleCalendarService>();

// Adaugă configurările din appsettings.json
builder.Services.AddSingleton<IConfiguration>(builder.Configuration);

builder.Services.AddControllers();

// Configurare Swagger/OpenAPI
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.AddSecurityDefinition("Bearer", new Microsoft.OpenApi.Models.OpenApiSecurityScheme
    {
        Name = "Authorization",
        Type = Microsoft.OpenApi.Models.SecuritySchemeType.Http,
        Scheme = "Bearer",
        BearerFormat = "JWT",
        In = Microsoft.OpenApi.Models.ParameterLocation.Header,
        Description = "Enter the JWT token received from a Login request.",
    });

    options.AddSecurityRequirement(new Microsoft.OpenApi.Models.OpenApiSecurityRequirement
    {
        {
            new Microsoft.OpenApi.Models.OpenApiSecurityScheme
            {
                Reference = new Microsoft.OpenApi.Models.OpenApiReference
                {
                    Type = Microsoft.OpenApi.Models.ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            Array.Empty<string>()
        }
    });
});

var app = builder.Build();

// Configurează pipeline-ul de request HTTP
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// CORS
app.UseStaticFiles();
app.UseRouting();
app.UseCors(AllowAllOrigins);

app.UseHttpsRedirection();
app.UseAuthorization();

app.MapControllers();

await app.RunAsync();

public partial class Program
{
    protected Program()
    { }
}
