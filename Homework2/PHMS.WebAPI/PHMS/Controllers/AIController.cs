using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using System.Net.Http;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

[ApiController]
[Route("api/[controller]")]
public class MedicalSpecializationController : ControllerBase
{
    private readonly HttpClient _httpClient;
    private readonly string _apiKey;
    private const string ApiUrl = "https://api.openai.com/v1/chat/completions";

    public MedicalSpecializationController(HttpClient httpClient, IConfiguration configuration)
    {
        _httpClient = httpClient;
        _apiKey = configuration["OpenAI:ApiKey"]; // Citește din appsettings.json
    }

    [HttpGet("{specialization}")]
    public async Task<IActionResult> GetSpecializationDescription(string specialization)
    {
        if (string.IsNullOrWhiteSpace(specialization))
        {
            return BadRequest("Specializarea nu poate fi goală.");
        }

        var requestBody = new
        {
            model = "gpt-4o-mini",
            messages = new[]
            {
                new { role = "system", content = "Ești un expert în domeniul medical." },
                new { role = "user", content = $"Descrie pe scurt specializarea medicală {specialization}." }
            },
            temperature = 0.7,
            max_tokens = 1000
        };

        string jsonContent = JsonSerializer.Serialize(requestBody);
        HttpContent httpContent = new StringContent(jsonContent, Encoding.UTF8, "application/json");

        _httpClient.DefaultRequestHeaders.Clear();
        _httpClient.DefaultRequestHeaders.Add("Authorization", $"Bearer {_apiKey}");

        HttpResponseMessage response = await _httpClient.PostAsync(ApiUrl, httpContent);
        string responseContent = await response.Content.ReadAsStringAsync();

        if (!response.IsSuccessStatusCode)
        {
            return StatusCode((int)response.StatusCode, $"Eroare API: {responseContent}");
        }

        using JsonDocument doc = JsonDocument.Parse(responseContent);
        string description = doc.RootElement
            .GetProperty("choices")[0]
            .GetProperty("message")
            .GetProperty("content")
            .GetString();

        return Ok(new { specialization, description });
    }
}
